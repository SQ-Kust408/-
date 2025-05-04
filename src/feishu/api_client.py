import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from MultiAgent.src.utils.config_loader import get_config
from MultiAgent.src.utils.logger import logger
from MultiAgent.src.feishu.message_templates import FeishuMessageTemplates
config = get_config("feishu")

class FeishuClient:
    def __init__(self):
        # 初始化飞书客户端
        self.client = lark.Client.builder() \
            .app_id(config["app_id"]) \
            .app_secret(config["app_secret"]) \
            .log_level(lark.LogLevel.DEBUG if get_config("system")["debug_mode"] else lark.LogLevel.WARN) \
            .build()

    def send_device_repair_message(self, user_id: str, device_model: str, issue: str):
        """使用设备报修模板发送消息"""
        message = FeishuMessageTemplates.device_repair_notification(device_model, issue)
        return self.send_generic_message(user_id, message)

    def send_contract_review_message(self, user_id: str, contract_type: str, reviewer: str, deadline: str):
        """使用合同审查模板发送消息"""
        message = FeishuMessageTemplates.contract_review_feedback(contract_type, reviewer, deadline)
        return self.send_generic_message(user_id, message)

    def send_generic_message(self, user_id: str, message_content: Dict):
        """发送文本消息到飞书"""
        try:
            """通用消息发送方法（支持所有模板）"""
            request = CreateMessageRequest.builder() \
                .receive_id_type(get_config("feishu")["receive_id_type"]) \
                .request_body(CreateMessageRequestBody.builder()
                              .receive_id(user_id)
                              .msg_type(message_content["msg_type"])
                              .content(message_content.get("content", "{}"))  # 处理content不存在的情况
                              #.uuid(lark.UUID.generate())
                              .build()) \
                .build()
            response = self.client.im.v1.message.create(request)
            if not response.success():
                logger.error(f"飞书消息发送失败：{response.msg}")
                return {"errcode": response.code, "errmsg": response.msg}
            logger.info(f"飞书消息发送成功，message_id: {response.data.message_id}")
            return {"errcode": 0, "message_id": response.data.message_id}
        except Exception as e:
            logger.error(f"飞书API调用异常：{str(e)}")
            return {"errcode": -1, "errmsg": str(e)}