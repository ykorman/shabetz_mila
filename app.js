(function() {
	$("#loginBtn").click(function() {
		username = $("#username").val();
		password = $("#password").val();
		$.post("shabetz_mila/login",
			{ username: username, password: password },
			function(data) {
			alert("Data loaded: " + data); });
	});
})();
