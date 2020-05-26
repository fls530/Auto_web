class LoginCase:
    """登录功能的用例数据"""
    # 正常登录的用例
    success_case_data = [
        {'mobile': "18684720553", "pwd": "python", "expected": "登录成功"},
    ]
    # 异常的用例数据：错误提示在页面上
    error_case_data = [
        {'mobile': "", "pwd": "python1", "expected": "请输入手机号"},
        {'mobile': "1868472055a", "pwd": "python1", "expected": "请输入正确的手机号"},
        {'mobile': "18684720553", "pwd": "", "expected": "请输入密码"}
    ]
    # 异常的用例数据，错误提示在弹窗中
    error_alert_data = [
        {'mobile': "18684720553", "pwd": "pyt1234", "expected": "帐号或密码错误!"},
        {'mobile': "18684727888", "pwd": "python1", "expected": "此账号没有经过授权，请联系管理员!"},
    ]


class InvestData:
    """投资功能的用来数据"""
    # 投资成功
    success_data = [
        {'title': '投资成功', 'money': 200, 'expected': '投标成功！'}
    ]
    # 投资失败投标置灰  非100整数倍且大于100，非100整数倍且小于100，字母，符号
    error_data = [
        {'title': '输入金额非10的整数倍', 'money': 456, 'expected': '请输入10的整数倍'},
        {'title': '输入金额为字母', 'money': 'a', 'expected': '请输入10的整数倍'},
        {'title': '输入金额为特殊字符', 'money': '$', 'expected': '请输入10的整数倍'}
    ]
    # 投资失败弹框提示  负数100整数倍金额，0，空格，100整数倍且小于100,投标的金额大于标剩余金额，购买标的金额大于标总金额，投标金额大于可用金额
    error_popup_data = [
        {'title': '输入金额为负数', 'money': -10, 'expected': '请正确填写投标金额'},
        {'title': '输入金额为0', 'money': 0, 'expected': '请正确填写投标金额'},
        {'title': '输入金额为空格', 'money': ' ', 'expected': '请正确填写投标金额'},
        {'title': '输入金额为10的整数倍，但少于100', 'money': 50, 'expected': '投标金额必须为100的倍数'},
    ]
