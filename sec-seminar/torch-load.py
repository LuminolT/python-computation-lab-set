import io
import torch
import base64

try:
    base64_string = input("Send model")
    bytes_data = base64.b64decode(base64_string)
    print(bytes_data)

    print('Evaluating the model ...')
    device = torch.device("cpu")
    model = torch.load(io.BytesIO(bytes_data), map_location=device)
    model.eval()
    print("Finished evaluating the model")
except Exception as e:
    print(f"oops, something went wrong: {e}")
