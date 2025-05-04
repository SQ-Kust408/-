from MultiAgent.src.intent.classifier import ChineseIntentClassifier
from MultiAgent.src.feishu.api_client import FeishuClient
from MultiAgent.src.utils.config_loader import get_config
from MultiAgent.src.feishu.message_templates import FeishuMessageTemplates

feishu_config = get_config("feishu")
huggingface_config = get_config("huggingface")
system_config = get_config("system")


def extract_device_repair_params(user_input: str) -> dict:
    """简单参数抽取示例（设备报修场景）"""
    params = {}
    if "设备" in user_input and "无法" in user_input:
        params["device_model"] = "M200"
        params["issue"] = user_input.split("：")[-1] if "：" in user_input else user_input
    return params


def process_user_input(user_input: str, user_id: str = None) -> str:
    """主处理流程：意图识别→参数抽取→模板消息发送"""
    # 1. 意图识别
    classifier = ChineseIntentClassifier()
    intent = classifier.predict(user_input)
    print(f"识别意图：{intent}")

    # 2. 生成消息内容
    if intent == "设备报修":
        # 设备报修处理
        params = extract_device_repair_params(user_input)
        message_content = FeishuMessageTemplates.device_repair_notification(
            device_model=params.get("device_model", "未知型号"),
            issue=params.get("issue", "无具体故障描述"),
        )
        response_content = f"已记录设备报修：{params.get('device_model', '未知')}，故障：{params.get('issue', '无')}"

    elif intent == "合同审查":
        # 合同审查处理
        message_content = FeishuMessageTemplates.generic_consultation_response(
            query=user_input,
        )
        response_content = f"合同审查意图已识别，输入内容：{user_input}"

    elif intent == "订单查询":  # 新增订单查询处理分支
        # 示例：假设参数为订单号
        order_id = user_input.split("订单")[-1].strip() or "未知订单号"
        message_content = FeishuMessageTemplates.order_status_update(
            order_id=order_id,
            status="处理中",  # 实际需调用ERP系统获取
            tracking_number="SF123456"  # 示例快递单号
        )
        response_content = f"订单查询已受理：订单号 {order_id}，状态：处理中"

    else:  # 通用咨询
        message_content = FeishuMessageTemplates.generic_consultation_response(
            query=user_input,
            suggestion="如需进一步帮助，请提供更多细节"
        )
        response_content = f"您的意图：{intent}，输入内容：{user_input}"

    # 3. 发送飞书消息
    feishu_client = FeishuClient()
    user_id = user_id or feishu_config["default_user_id"]
    feishu_client.send_generic_message(user_id, message_content)
    return response_content


if __name__ == "__main__":
    print("=== Agent系统启动 ===")
    print("请输入您的需求（输入q退出）：")

    while True:
        user_input = input("> 请输入：").strip()

        # 退出条件
        if user_input.lower() == "q":
            print("系统已退出")
            break

        # 输入校验
        if not user_input:
            print("输入不能为空，请重新输入")
            continue

        # 处理输入
        try:
            result = process_user_input(user_input)
            print(f"处理结果：{result}")
            print("飞书消息已发送，请注意查收！\n")
        except Exception as e:
            print(f"处理失败：{str(e)}，请检查配置或网络\n")