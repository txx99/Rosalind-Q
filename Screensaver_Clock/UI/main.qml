// main.qml
// this is user interface info
//COMMENTS like javascript, use two /


import QtQuick
import QtQuick.Controls.Basic
//careful of spelling


ApplicationWindow {
//creating an application window
	visible: true
	width: 500
	height: 400
	title: "WelcomeApp"
	property string currTime: "00:00:00"   //using this in qml so it chnages in all places where used 
	property QtObject backend   //creates QtObject to hold py obj back_end
	Rectangle {
		anchors.fill: parent   //fills the parent window entirely
		Image {
			sourceSize.width: parent.width
			sourceSize.height: parent.height
			source: "\IMG_5793"  // gets suffixed to current directory location
			fillMode: Image.PreserveAspectCrop}
		Rectangle {
			anchors.fill: parent
			color: "transparent" //second rectangle goes over the first rectangle, but transparent beside sthe text so we still see the image underneath; if not transparent, will fill entire AppWindow
			Text {
				anchors{
					bottom: parent.bottom
					bottomMargin: 12
					left: parent.left
					leftMargin: 12}
				text: currTime
				font.pixelSize: 50
				color: "black"}}}
		Connections{
			target: backend
			function onUpdated(msg){
				currTime=msg;}
			}
		}
//without threading, UI will freeze. need threading and not multiprocessing here.
//will create 2 func: 1 for threading, 1 for mutltiprocessing


// now, making a signal handler to receive updated signal/updater function.
//signal handler uses 'on' prefix to signal name, and capitalises first letter of signal name. ex. mysignal -> onMysignal.  yourSign ->onYourSign.

//small apps like this dont need separate calls for differnet signals but big apps do.
//we will use 1/10 of a second delay (for what??)

//creating a Rectangle Type inside the app window that takes up the whole window space
//creating an image inside the Rectangle
//creating a secomd rectangle overlayed on the previous Rectangle that says the current time


//	Text {	anchors.centerIn: parent
//		text: "Bienvenue, tazmeen~"
//		font.pixelSize: 32}}

//careful of punctuation ! fullstop. colon: slash/