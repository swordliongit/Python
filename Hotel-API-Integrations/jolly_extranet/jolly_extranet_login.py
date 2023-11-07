import requests

from pyquery import PyQuery as pq
from headers import headers, headers2, headers3


def Login(session):
    login_page = session.get("https://extranet.jollytur.ws/Dashboard", headers=headers)
    login_result = pq(login_page.content.decode("utf-8"))
    token = login_result.find('input[name="__RequestVerificationToken"]').attr("value")
    return_url = login_result.find('input[name="ReturnUrl"]').attr("value")

    data = {
        "ReturnUrl": return_url,
        "ScopeCode": "PEN333",
        "Username": "kanal@snapturizm.com.tr",
        "Password": "snap23",
        "LanguageId": "1",
        "__RequestVerificationToken": token,
        "RememberLogin": "false",
    }

    login_post = session.post(login_page.url, headers=headers2, data=data)

    login_param = pq(login_post.content.decode("utf-8"))

    data = {
        "code": login_param.find('input[name="code"]').attr("value"),
        "id_token": login_param.find('input[name="id_token"]').attr("value"),
        "scope": "openid email profile corporate_profile offline_access",
        "state": login_param.find('input[name="state"]').attr("value"),
        "session_state": login_param.find('input[name="session_state"]').attr("value"),
    }

    session.post(
        "https://extranet.jollytur.ws/signin-oidc", headers=headers3, data=data
    )

    return session
