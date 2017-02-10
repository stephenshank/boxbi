#PLC

Application for communicating with PLCs.

## Getting started

Obtain the JSON files and place them in the `data` directory. Run

```
python manage.py migrate
python manage.py loaddata
```

to populate data.

To start the server, run

```
python manage.py runserver 0.0.0.0:8000
```

and then visit `http://localhost:8000/test` in a web browser.

## API

### Testing (/test/)

Simple test to ensure functionality; should return

	{
		"status": 1
	}

### PLC (/plc/{ip})

Communicate with PLCs. Here `{ip}` should be `db`, `glue`, or `starch`.