OBS_PROJECT := EA4
OBS_PACKAGE := ea-re2c
DISABLE_BUILD := repository=CentOS_6.5_standard repository=CentOS_7 repository=CentOS_9
include $(EATOOLS_BUILD_DIR)obs.mk
