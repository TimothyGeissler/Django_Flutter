import 'dart:convert';
import 'package:json_annotation/json_annotation.dart';

part 'Superhero.g.dart';

@JsonSerializable()

class Superhero {
  final String name;
  final String alias;

  Superhero(this.name, this.alias);

  /// A necessary factory constructor for creating a new User instance
  /// from a map. Pass the map to the generated `_$UserFromJson()` constructor.
  /// The constructor is named after the source class, in this case, User.
  factory Superhero.fromJson(Map<String, dynamic> json) => _$SuperheroFromJson(json);

  /// `toJson` is the convention for a class to declare support for serialization
  /// to JSON. The implementation simply calls the private, generated
  /// helper method `_$UserToJson`.
  Map<String, dynamic> toJson() => _$SuperheroToJson(this);
  /*
  Hero.fromJson(Map<String, dynamic> json):
    name = json['name'],
    alias = json['alias'];

  Map<String, dynamic> toJson() => {
    'name': name,
    'alias': alias
  };*/
}
