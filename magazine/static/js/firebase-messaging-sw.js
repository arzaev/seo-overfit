importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.8.1/firebase-messaging.js');

var firebaseConfig = {
	apiKey: "AIzaSyC_IaWIemvsvQv5qJmO76SIpOEgiSTddIE",
	authDomain: "overfitness-6da7d.firebaseapp.com",
	databaseURL: "https://overfitness-6da7d.firebaseio.com",
	projectId: "overfitness-6da7d",
	storageBucket: "overfitness-6da7d.appspot.com",
	messagingSenderId: "362909612421",
	appId: "1:362909612421:web:3f9a6f5b5d877b09"
};

firebase.initializeApp(firebaseConfig);

const messaging = firebase.messaging();
messaging.setBackgroundMessageHandler(function(payload) {
	var notification = JSON.parse(payload.data.notification);
	const title = notification['title'];
	const options = {
		body: notification['body'],
		icon: notification['icon']
	};
	return self.registration.showNotification(title, options);
});

