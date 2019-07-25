String ritual = " ";

void setup() {
  size(700, 300);
}

void draw() {
  //background(0);
}
void mousePressed() {
  color [] yum = {#F7DC3C, #E48CFC, #91E6E8, #FCCA40, #C58FF5};
  int textcolor = int(random(0, yum.length));
  background(yum[textcolor]);
  String[] adj = {"ugly ", "lazy ", "charming ", "tasty ", "messy ", "sad ", "orange ", "silly ", "sparkly"};
  String[] place = {"pineapple", "cottage", "apartment", "school bus", "local park"};
  String[] verbTransportation = {"jump ", "run ", "scooter ", "drive ", "swim "};
  String[] noun = { "toothbrush", "meds", "socks","cat", "bra"};
  String[] verb = { "pet", "bake", "burn", "put on", "touch"};
  String[] adverb = { "gently" ,"carefully", "tastefully", "hastily" ,"cheerfully"};

  int adj1 = int(random(0, adj.length));
  int noun1 = int(random(0, noun.length));
  int adj3 = int(random(0, adj.length));
  int noun2 = int(random(0, noun.length));
  int verbT = int(random(0, verbTransportation.length));
  int verb1 = int(random(0, verb.length));
  int place1 = int(random(0, place.length));
  int adverb1 = int(random(0, adverb.length));
  int place2 = int(random(0, place.length));

  ritual = "wake up in your " + adj[adj1] + place[place1] + ". " 
  +  verb[verb1]+ " your " + noun[noun2] + " " + adverb[adverb1]+ ". "  
  + verbTransportation[verbT] + " to your " + place[place2]+ ". " ;

  //delay(1000);
  text(ritual, 10, 20);
}
