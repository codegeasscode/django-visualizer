import json
from django.shortcuts import render
from .utils import generate_visualization

def visualise(request):
    visualizations = []
    error_message = None  # error msg

    if request.method == "POST":
        json_data = request.POST.get("json_data", "").strip()

        # json_data
        # [
        #     {
        #         "id": "1",
        #         "name": "Example Bar",
        #         "data": [[1, 2, 3], [10, 20, 30]],
        #         "type": "bar"
        #     },
        #     {
        #         "id": "2",
        #         "name": "Example Table",
        #         "data": [{"Name":"Alok", "Dept":"Backend"}, {"Name":"Binu", "Dept":"Manager"}, {"Name":"Rahul", "Dept":"Frontend"}],
        #         "type": "table"
        #     }
        # ]

        # validate empty json
        if not json_data:
            error_message = "Empty Json"

        else:
            try:
                data_list = json.loads(json_data)  

                if not isinstance(data_list, list):
                    error_message = "input JSON must be a list of objects."
                else:
                    for item in data_list:
                        if not isinstance(item, dict) or "type" not in item or "data" not in item:
                            error_message = "each object must have 'type' and 'data' fields."
                            break  

                if not error_message:
                    visualizations = generate_visualization(data_list)

            except json.JSONDecodeError:
                error_message = "Invalid JSON"
            except Exception as e:
                print(e)
                error_message = "Something Went Wrong"

    return render(request, "visualise.html", {"visualizations": visualizations, "error_message": error_message})
