from typing import Dict, Any


class FeishuMessageTemplates:
    """飞书消息模板库（支持多种消息类型）"""

    @staticmethod
    def device_repair_notification(device_model: str, issue: str, contact_time: str = "2小时内") -> Dict[str, Any]:
        """设备报修通知模板（文本消息）"""
        return {
            "msg_type": "text",
            "content": f'{{"text":"已收到设备报修：\\n型号：{device_model} \\n故障：{issue} \\n工程师将在{contact_time}联系您"}}'
        }

    @staticmethod
    def contract_review_feedback(contract_type: str, reviewer: str, deadline: str) -> Dict[str, Any]:
        """合同审查反馈模板（富文本Markdown）"""
        return {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": f"合同审查进度：{contract_type}",
                        "content": [
                            [{"tag": "text", "text": "已分配专员："}],
                            [{"tag": "text", "text": reviewer, "markdown": {"bold": True}}],
                            [{"tag": "text", "text": f"\\n审查截止时间：{deadline}"}]
                        ]
                    }
                }
            }
        }

    @staticmethod
    def order_status_update(order_id: str, status: str, tracking_number: str) -> Dict[str, Any]:
        """订单状态更新模板（卡片消息）"""
        return {
            "msg_type": "interactive",
            "content": {
                "config": {"wide_screen_mode": True},
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": f"### 订单 {order_id} 状态更新\\n**当前状态**：{status}\\n**快递单号**：{tracking_number}"
                        }
                    },
                    {
                        "tag": "action",
                        "actions": [
                            {
                                "tag": "button",
                                "text": {"tag": "text", "text": "查看物流详情"},
                                "type": "primary",
                                "url": f"https://example.com/tracking?order_id={order_id}"
                            }
                        ]
                    }
                ]
            }
        }

    @staticmethod
    def generic_consultation_response(query: str, suggestion: str = "请提供更多细节") -> Dict[str, Any]:
        """通用咨询响应模板（文本消息）"""
        return {
            "msg_type": "text",
            "content": f'{{"text":"您的咨询已收到：\\n\\n{query}\\n\\n{suggestion}"}}'
        }