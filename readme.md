# Generador PDF

Endpoint para generar reportes en pdf

## System Requirements
#### To run this project you need:
* [Python3.7.5](https://www.python.org/downloads/release/python-375/)

#### Suggested:
* [Postman](https://www.postman.com/downloads/)

## Package Manager
The project was build under **pipenv** enviroment manager, you might use the next commands:
* To create/ativate a virtual enviroment, place yourself on the project directory and run:
```
pipenv shell
```
* To install project requirements:
```
pipenv install -r ./requirements.txt
```

## Run server
```
python manage.py runserver
```

## Testing with Postman
Once you run the run server command:
1. Open Postman 
2. Write down **http://localhost:8000/generate_pdf** url
3. On the **body** tab, select **raw** option and in the dropdown menu select **JSON (application/json)** option.
4. Here is an example of a valid payload:
```
{
    "report": "dcjMoneyBox",
    "name": "David Cruz",
    "rfc": "ABCD1234561A1",
    "address": "Avenida calle no real, Colonia Fake para pruebas, Random, RealFake",
    "user": "abA12ab",
    "currency": "Moneda nacional",
    "plan": "Semanal",
    "period": "22/03/20-18/04/2020",
    "goal": "coche",
    "data": [
        ["Paypal", "50.00 MXN", "16/01/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/02/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/03/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/04/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/05/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/06/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/07/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/08/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/09/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/10/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/11/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/12/2020 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/01/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/02/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/03/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/04/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/05/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/06/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/07/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/08/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/09/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/10/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/11/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/12/2021 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/01/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/02/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/03/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/04/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/05/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/06/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/07/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/08/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/09/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/10/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/11/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/12/2022 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/01/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/02/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/03/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/04/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/05/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/06/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/07/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/08/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/09/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/10/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/11/2023 14:44", "0.25 MXN", "50.25"],
        ["Paypal", "50.00 MXN", "16/12/2023 14:44", "0.25 MXN", "50.25"]
    ],
    "total": "351.75 MXN"
}
```
5. You'll find a pdf in the root of project or can downloaded directly from postman if all the process is done correctly.