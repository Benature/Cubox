# 定义变量
CONFIG_FILE := config.py
TEMPLATE_FILE := config_template.py

# 检查是否需要复制文件
NEED_COPY := $(shell [ ! -f "$(CONFIG_FILE)" ] && echo "true")

# 如果需要复制文件，则执行复制操作
ifeq ($(NEED_COPY),true)
    $(shell cp "$(TEMPLATE_FILE)" "$(CONFIG_FILE)")
    $(info Copied $(TEMPLATE_FILE) to $(CONFIG_FILE), please remember to modify your config file.)
else
    # $(info $(CONFIG_FILE) already exists.)
endif


run:
	@ nohup python api.py > flask.log 2>&1 &

status:
	@ ps -ef | grep "python api.py"

kill:
	@-pkill -f "python api.py" -e ||:
	@echo "Finish killing"


install:
	pip3 install -r requirements.txt


# .PHONY: 