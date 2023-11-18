Api.sendChatAction({
  chat_id: chat.chatid,
  action: "typing"
})
Api.sendChatAction({
  chat_id: chat.chatid,
  action: "typing"
})
HTTP.get({
  url: "https://weather.apinepdev.workers.dev/?cityname=" +
    message +
    "",
  success: "/success"})
var result = JSON.parse(content)
var name = result.location.name
var region = result.location.region
var country = result.location.country
var temp = result.current.temp_c
var lastu = result.current.last_updated
var text = result.current.condition.text
var lati = result.location.lat
var longi = result.location.lon
var wind_kph = result.current.wind_kph
var wd = result.current.wind_degree
var hum = result.current.humidity
var c = result.current.cloud
var gmph = result.current.gust_mph
var gkph = result.current.gust_kph
if (name == undefined) {
  Bot.sendMessage("Error")
} else {
  Bot.sendMessage(
    "*🌤️ Weather Deatails \n\nName: " +
      name +
      "\n\n🌅Region: " +
      region +
      "\n\n🇧🇩Country: " +
      country +
      "\n\n🌡️Temperature: " +
      temp +
      "° C\n\n💭Wind speed: " +
      wind_kph +
      " kp/h\n\n🌬️Wind degree: " +
      wd +
      "\n\n🧞Humidity: " +
      hum +
      "\n\n☁️Cloud: " +
      c +
      "\n\n🤧weather description: " +
      text +
      " \n\n😵‍💫Last updated : " +
      lastu +
      "\n\n☁️Latitude: " +
      lati +
      "\n\n☁️Longitude: " +
      longi +
      "\n\n⚡️Gust_mph: " +
      gmph +
      "\n\n⚡Gust_kph: " +
      gkph +
      "*"
  )
}
