String ritualL1 = " ";
String ritualL2 = " ";
String ritualL3 = " ";
String ritualL4 = " ";

void setup() {
  size(300, 300);
}

void draw() {
  //background(0);
}
void mousePressed() {
  //color [] yum = {#F7DC3C, #E48CFC, #91E6E8, #FCCA40, #C58FF5};
  //int textcolor = int(random(0, yum.length));
  //background(yum[textcolor]);
  background(255);
  //int textcolor = 0;
  String[] adj = {"ugly ", "lazy ", "charming ", "tasty ", "messy ", "sad ", "orange ", "silly ", "sparkly "};
  String[] place = {"pineapple", "cottage", "apartment", "school bus", "local park", "workplace"};
  String[] verbTransportation = {"jump ", "run ", "scooter ", "drive ", "swim "};
  String[] noun = { "toothbrush", "meds", "socks","cat", "bra"};
  String[] verb = { "pet", "bake", "burn", "put on", "touch"};
  String[] adverb = { "gently" ,"carefully", "tastefully", "hastily" ,"cheerfully"};
  String[] verbNoObj = { "cry", "think", "run", "sit", "hide", "begin", "contemplate"};

  int adj1 = int(random(0, adj.length));
  int noun1 = int(random(0, noun.length));
  int adj3 = int(random(0, adj.length));
  int noun2 = int(random(0, noun.length));
  int verbT = int(random(0, verbTransportation.length));
  int verb1 = int(random(0, verb.length));
  int place1 = int(random(0, place.length));
  int adverb1 = int(random(0, adverb.length));
  int place2 = int(random(0, place.length));
  int vNoObj1 = int(random(0, verbNoObj.length));
  

  ritualL1 = "wake up in your " + adj[adj1] + place[place1] + ". " ;
  ritualL2 = verb[verb1]+ " your " + noun[noun2] + " " + adverb[adverb1]+ ". " ; 
  ritualL3 = verbTransportation[verbT] + " to your " + place[place2]+ ". "; 
  ritualL4 = verbNoObj[vNoObj1] + ". ";

  //delay(1000);
  fill(0);
  text(ritualL1, 10, 20);
  text(ritualL2, 10, 40);
  text(ritualL3, 10, 60);
  text(ritualL4, 10, 80);
}
