run:
	@ nohup python api.py > flask.log 2>&1 &

status:
	@ ps -ef | grep "python api.py"

kill:
	@-pkill -f "python api.py" -e ||:
	@echo "Finish killing"


install:
	pip3 install -r requirements.txt


.PHONY: 