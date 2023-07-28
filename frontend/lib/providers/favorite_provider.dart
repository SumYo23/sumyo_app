import 'package:flutter/material.dart';
import 'package:v2/providers/token_provider.dart';

import '../models/food_model.dart';
import '../repositories/favorite_repository.dart';
import '../repositories/token_repository.dart';

class FavoriteProvider extends ChangeNotifier {

  List<Food> _favorites = [];

  final FavoriteRepository favoriteRepository;

  FavoriteProvider({required this.favoriteRepository});

  List<Food> get favorites => _favorites;
  Future<void> getFavorite() async {
    _favorites = await favoriteRepository.fetchFavorite();
    notifyListeners();
  }
  Future<void> ADDFavorite(Food food) async {
    await favoriteRepository.addFavorite(food);
    notifyListeners();
  }
  Future<void> DELFavorite(Food food) async {
   await favoriteRepository.delFavorite(food);
    notifyListeners();
  }
}
