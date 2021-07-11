$(document).ready(
    function(){
        const form = document.join;
        $("form[name=join]").on(
            "submit",
            function(event) {
                if($("input[name=name]").val() == "") {
                   form.name.style.borderColor = '#FF0000';
                   document.getElementById('alert_name').innerText = "실명을 입력해주세요";
                }else{
                    form.name.style.borderColor = '#5193F0';
                    document.getElementById('alert_name').innerText = "";
                }
                if($("input[name=nickname]").val() == "") {
                    form.nickname.style.borderColor = '#FF0000';   
                    document.getElementById('alert_nickname').innerText = "페이지 내에서 사용되는 활동명입니다";
                }else{
                    form.nickname.style.borderColor = '#5193F0';
                    document.getElementById('alert_nickname').innerText = "";
                }
                if($("input[name=email]").val() == "") {
                    form.email.style.borderColor = '#FF0000';
                    document.getElementById('alert_email').innerText = "학교 이메일 주소를 입력해주세요";
                }else{
                    form.email.style.borderColor = '#5193F0';
                    document.getElementById('alert_email').innerText = "";
                }
                if($("input[name=loginPw]").val() == "") {
                    form.loginPw.style.borderColor = '#FF0000';
                    document.getElementById('alert_login').innerText = "비밀번호를 입력해주세요";
                }else{
                    form.loginPw.style.borderColor = '#5193F0';
                    document.getElementById('alert_login').innerText = "";
                }
                return false;
            }
        )

        const login = document.login;
        $("form[name=login]").on(
            "submit",
            function(event) {
                if($("input[name=id]").val() == "") {
                    login.id.style.borderColor = '#FF0000';
                    document.getElementById('alert_id').innerText = "이메일 주소를 입력해주세요.";
                }else{
                    login.id.style.borderColor = '#5193F0';
                    document.getElementById('alert_id').innerText = "";
                }
                if($("input[name=password]").val() == "") {
                    login.password.style.borderColor = '#FF0000';
                    document.getElementById('alert_pwd').innerText = "비밀번호를 입력해주세요.";
                }else{
                    login.password.style.borderColor = '#5193F0';
                    document.getElementById('alert_pwd').innerText = "";
                }
                return false;
            }
        )




    }   //function()
)   //ready()