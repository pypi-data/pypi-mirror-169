from openhab import ItemEvent
from openhab import CRUD
import json
import paho.mqtt.client as mqtt
import string
import random

class EventBus(object):
    def __init__(self, openhab_url: str = "http://127.0.0.1:8080", openhab_username: str = None, openhab_password: str = None, mqtt_ip: str = "127.0.0.1", mqtt_port: int = 1883, mqtt_username: str = None, mqtt_password: str = None, statePublishTopic: str = None, commandPublishTopic: str = None, stateSubscribeTopic: str = None, commandSubscribeTopic: str = None):
        self.openhab_url: str = openhab_url
        self.openhab_username: str = openhab_username
        self.openhab_password: str = openhab_password
        self.mqtt_ip: str = mqtt_ip
        self.mqtt_port: int = mqtt_port
        self.mqtt_username: str = mqtt_username
        self.mqtt_password: str = mqtt_password
        self.statePublishTopic: str = None
        self.commandPublishTopic: str = None
        self.stateSubscribeTopic: str = None
        self.commandSubscribeTopic: str = None
        self.__topics = []
        self.__qos = 0

        if statePublishTopic == stateSubscribeTopic:
            raise ValueError('statePublishTopic and stateSubscribeTopic should be not equal!')

        if commandPublishTopic == commandSubscribeTopic:
            raise ValueError('commandPublishTopic and commandSubscribeTopic should be not equal!')

        if statePublishTopic is not None and commandPublishTopic is None:
            if "${item}" not in statePublishTopic:
                raise ValueError('statePublishTopic needs ${item} as placeholder for your items')
            self.statePublishTopic = statePublishTopic
            self.commandPublishTopic = None
        elif statePublishTopic is None and commandPublishTopic is not None:
            if "${item}" not in commandPublishTopic:
                raise ValueError('commandPublishTopic needs ${item} as placeholder for your items')
            self.statePublishTopic = None
            self.commandPublishTopic = commandPublishTopic
        else:
            self.statePublishTopic = "openhab/${item}/state"
            self.commandPublishTopic = None

        if stateSubscribeTopic is not None and commandSubscribeTopic is None:
            if "${item}" not in stateSubscribeTopic:
                raise ValueError('stateSubscribeTopic needs ${item} as placeholder for your items')
            self.stateSubscribeTopic = stateSubscribeTopic
            self.commandSubscribeTopic = None
        elif stateSubscribeTopic is None and commandSubscribeTopic is not None:
            if "${item}" not in commandSubscribeTopic:
                raise ValueError('commandSubscribeTopic needs ${item} as placeholder for your items')
            self.stateSubscribeTopic = None
            self.commandSubscribeTopic = commandSubscribeTopic
        else:
            self.stateSubscribeTopic = None
            self.commandSubscribeTopic = "openhab/${item}/state"

        if openhab_username is not None and openhab_password is not None:
            self.__crud = CRUD(self.openhab_url, self.openhab_username, self.openhab_password)
            self.__item_event = ItemEvent(self.openhab_url, self.openhab_username, self.openhab_password)
        else:
            self.__crud = CRUD(self.openhab_url)
            self.__item_event = ItemEvent(self.openhab_url)

        self.__items = self.__crud.getAllItems()

        for item in self.__items:
            if self.commandSubscribeTopic:
                tpc = self.commandSubscribeTopic.replace("${item}", str(item.get("name")))
                self.__topics.append((tpc, self.__qos))

            if self.stateSubscribeTopic:
                tpc = self.stateSubscribeTopic.replace("${item}", str(item.name))
                self.__topics.append((tpc, self.__qos))

        client_pre = "openHAB"
        client_post = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        client_name = client_pre[:20] + client_post

        self.__client = mqtt.Client(client_id=client_name, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")

        if self.mqtt_username is not None and self.mqtt_password is not None:
            self.__client.username_pw_set(username=self.mqtt_username,password=self.mqtt_password)
        else:
            self.__client.username_pw_set(None)

        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

        self.__client.connect(self.mqtt_ip, self.mqtt_port)
        self.__publish()
        self.__client.loop_forever()

    def __on_connect(self, client, userdata, flags, rc):
        self.__client.subscribe(self.__topics)

    def __on_message(self, client, userdata, msg):
        topic = msg.topic
        stateOrCommand = str(msg.payload.decode("utf-8"))

        if self.stateSubscribeTopic:
            itemPosition = self.stateSubscribeTopic.split("${item}")[0].count("/")
            item_name = topic.split("/")[itemPosition]
            self.__crud.postUpdate(item_name, str(stateOrCommand))

        if self.commandSubscribeTopic:
            itemPosition = self.commandSubscribeTopic.split("${item}")[0].count("/")
            item_name = topic.split("/")[itemPosition]
            self.__crud.sendCommand(item_name, str(stateOrCommand))

    def __publish(self):
        if self.statePublishTopic:
            response = self.__item_event.ItemStateEvent()
            mqtt_topic = self.statePublishTopic

        if self.commandPublishTopic:
            response = self.__item_event.ItemCommandEvent()
            mqtt_topic = self.commandPublishTopic

        with response as events:
            for line in events.iter_lines():
                line = line.decode()

                if "data" in line:
                    line = line.replace("data: ", "")

                    try:
                        data = json.loads(line)
                        topic = data.get("topic")
                        event_item_name = topic.split("/")[2]

                        mqtt_topic.replace("${item}", event_item_name)

                        if self.statePublishTopic:
                            stateOrCommand = self.__crud.getState(event_item_name)

                        if self.commandPublishTopic:
                            payload = json.loads(data.get("payload"))
                            stateOrCommand = payload.get("value")

                        self.__client.publish(mqtt_topic, payload=stateOrCommand, qos=self.__qos, retain=False)
                    except json.decoder.JSONDecodeError:
                        print("Event could not be converted to JSON")
