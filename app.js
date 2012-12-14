(function() {
	$("#loginBtn").click(function() {
		username = $("#username").val();
		password = $("#password").val();
		$.post("shabetz_mila/login",
			{ username: username, password: password },
			function(response) {
				if (response == "success") {
					$.mobile.changePage($("#main"));
					// alert($.cookie("username"));
				} else
					$("#loginError").popup("open");					
			});
	});
})();
