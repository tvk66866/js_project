//testing childprocess
// import child_process;
//import * as firebase from "firebase/app";
//var firebase = require("firebase/app");

////import firebase from "firebase"
////<script src="https://www.gstatic.com/firebasejs/7.14.2/firebase-app.js"></script>
//const firebaseConfig = {
//  apiKey: "AIzaSyBdCtKAQlpydwshdovRMabhfCKDlEgoFQ4",
//  authDomain: "vas-ml-fhir.firebaseapp.com",
//  databaseURL: "https://vas-ml-fhir.firebaseio.com",
//  projectId: "vas-ml-fhir",
//  storageBucket: "vas-ml-fhir.appspot.com",
//  messagingSenderId: "157728948296",
//  appId: "1:157728948296:web:165720b3830c063d26987d"
//};
//firebase-app.initializeApp(firebaseConfig);
//
//const messageAppReference = firebase-app.database();

$(function() { 
console.log('testing');
let $bp = $("#bpId")
let bp = document.querySelector("#bpId")
let $bh = $("#bhId")
let $ot = $("#otId")
let $tri = $("#triId")
let $hdl = $("#hdlId")
let $ldl = $("#ldlId")
let $tcl = $("#tclId")
let $a1c = $("#a1cId")
let $cre = $("#creId")
let $predId = $("#PredValue")
let $head = $("body h1")
let predictInput = {
	"Blood Pressure": $bp.val(),
	"Body Height": $bh.val(),
	"High Density Lipoprotein Cholesterol": $hdl.val(),
	"Low Density Lipoprotein Cholesterol": $ldl.val(),
	"Triglycerides": $tri.val(),
	"Total Cholesterol": $tcl.val(),
	"Oral temperature": $ot.val(),
	"Hemoglobin A1c_Hemoglobin_total in Blood": $a1c.val(),
	"Creatinine": $cre.val(),
}
// console.log($head.text())
$("#predB").click(function(event){
  event.preventDefault();
  console.log(bp.value)
  console.log($bp.val());
  console.log($ot.val());
  console.log($bh.val());
  console.log($tri.val());
  console.log($hdl.val());
  console.log($ldl.val());
  console.log($tcl.val());
  console.log($a1c.val());
  console.log($cre.val());
  
  
  predictInput["Blood Pressure"] = [$bp.val()];
  predictInput["Body Height"] = [$bh.val()];
  predictInput["High Density Lipoprotein Cholesterol"] = [$hdl.val()];
  predictInput["Low Density Lipoprotein Cholesterol"] = [$ldl.val()];
  predictInput["Triglycerides"] = [$tri.val()];
  predictInput["Total Cholesterol"] = [$tcl.val()];
  predictInput["Oral temperature"] = [$ot.val()];
  predictInput["Hemoglobin A1c_Hemoglobin_total in Blood"] = [$a1c.val()];
  predictInput["Creatinine"] = [$cre.val()];
  console.log(predictInput)

  let predictStringified = JSON.stringify(predictInput)
  console.log(predictStringified)
//  const messagesReference = messageAppReference.ref('vitals');
//  messagesReference.push(predictInput)
// 24.6.80.35  /127.0.0.1
  $.post("http://127.0.0.1:5000/receiver", JSON.stringify(predictInput)).done(function(response){
		console.log(response)
		$predId.text(response)
	});
  

});


});