from send_request import send_request

# ПЕРМЕННЫЕ----------------------------
data = {
    "x": 9,
    "y": 1
}

data = send_request("my/Falbue/action/move", data)