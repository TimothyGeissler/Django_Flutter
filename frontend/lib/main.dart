import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:frontend/models/Superhero/Superhero.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            RaisedButton(
              child: Text("API Call GET"),
              onPressed: () async {
                //make API call
                var url = 'http://10.0.2.2:8000/heroes/';
                var response = await http.get(url);
                print(response.body.toString());
                final List t = json.decode(response.body);
                final List<Superhero> hero_obj =
                t.map((item) => Superhero.fromJson(item)).toList();
                print(hero_obj[0].name);
              },
            ),
            RaisedButton(
              child: Text("API Call POST"),
              onPressed: () async {
                var url = 'http://10.0.2.2:8000/logins/';
                String username = 'timg', password = 'pass';
                String jsonBody = '{"email":$username,"password":$password}';
                var response = await http.post(
                  url,
                  headers: <String, String>{
                    'Content-Type': 'application/json',
                  },
                  body: jsonEncode(<String, String>{
                    'username': username,
                    'password': password,
                  })
                );
                print(response.statusCode);
              },
            ),
            RaisedButton(
              child: Text("API Login"),
              onPressed: () async {
                var url = 'http://10.0.2.2:8000/user_login/';
                String username = 'timdg', password = 'pass';
                var loginMap = new Map<String, dynamic>();
                loginMap['username'] = username;
                loginMap['password'] = password;
                var response = await http.post(
                    url,
                    body: loginMap
                );
                print(response.body + " : " + response.statusCode.toString());
              },
            ),
             RaisedButton(
               child: Text("API Signin"),
               onPressed: () async {
                 var url = 'http://10.0.2.2:8000/user_register/';
                 String username = 'timdg', password1 = 'Google15', password2 = "Google15";
                 var registerMap = new Map<String, dynamic>();
                 registerMap['username'] = username;
                 registerMap['password1'] = password1;
                 registerMap['password2'] = password2;
                 var response = await http.post(
                     url,
                     body: registerMap
                 );
                 print(response.body + " : " + response.statusCode.toString());
               },
             )
          ],
        ),
      ),
    );
  }
}
