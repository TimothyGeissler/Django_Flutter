// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'Superhero.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Superhero _$SuperheroFromJson(Map<String, dynamic> json) {
  return Superhero(
    json['name'] as String,
    json['alias'] as String,
  );
}

Map<String, dynamic> _$SuperheroToJson(Superhero instance) => <String, dynamic>{
      'name': instance.name,
      'alias': instance.alias,
    };
