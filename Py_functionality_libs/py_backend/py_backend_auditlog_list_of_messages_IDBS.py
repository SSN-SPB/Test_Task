#!/usr/bin/env python3
import requests
import json

SERVER = "https://custom-panel-deployment-qa.eu2.idbs-dev.com/"
ENDPOINT = SERVER + "custom-item-mgmt/api/v1/default-qatestenv/widgets"
# ENDPOINT = SERVER + 'custom-item-mgmt/api/v1/default-testing/widgets'
need_to_delete = True
# need_to_delete = False


def delete_widget(endpoint, bear_token):
    del_widget = requests.delete(
        endpoint,
        headers={"Content-Type": "application/json", "Authorization": bear_token},
    )
    print("Deleting range return code is {}".format(del_widget))


def get_list_of_widgets(get_endpoint, bear_token):
    getting_widgets = requests.get(
        get_endpoint,
        headers={"Content-Type": "application/json", "Authorization": bear_token},
    )
    print("Getting range return code is {}".format(getting_widgets))
    widgets_in_JSONformat = json.loads(getting_widgets.text)
    return widgets_in_JSONformat


def get_widgets_id(endpoint, token):
    widgets_id = []
    theJSONlist = get_list_of_widgets(endpoint, token)
    for i in theJSONlist:
        print(i["widgetId"])
        widgets_id.append(i["widgetId"])
    return widgets_id


def main(to_delete):
    # Setting token
    bear_token = "Bearer " + "6d0wF#$gX99saeW8&fpTs6!GM5jBxR$R"
    # bear_token = 'Bearer ' + 'P6c1nJ5osqZ0UnTqVJ#pqMfPRlw553F%'
    # hardcoded example range_to_delete = ['3b9-..', 'd1dfd8e4-c7b4-49aa-..']
    range_to_delete = get_widgets_id(ENDPOINT, bear_token)
    counter = 0

    for i in range_to_delete:
        counter = counter + 1
        end_point = ENDPOINT + "/" + i
        print(to_delete)
        if need_to_delete:
            delete_widget(end_point, bear_token)
    print("Totally {} widgets were found".format(counter))


if __name__ == "__main__":
    main(need_to_delete)
