api_py_path="api_cubox.py"

run:
	@ nohup python ${api_py_path} > flask.log 2>&1 &

status:
	@ ps -ef | grep "python ${api_py_path}"

kill:
	@-pkill -f "python ${api_py_path}" -e ||:
	@echo "Finish killing"


install:
	pip3 install -r requirements.txt


# .PHONY: 