import 'package:flutter/cupertino.dart';
import 'package:provider/provider.dart';
import 'package:v2/providers/token_provider.dart';
import '../models/food_model.dart';
import '../repositories/food_repository.dart';
import '../repositories/token_repository.dart';

class FoodProvider with ChangeNotifier {
  List<Food> _foods = [];

  final FoodRepository foodRepository;
  List<Food> get foods => _foods;
  FoodProvider({required this.foodRepository});

  Future<void> getFoods() async {
    _foods = await foodRepository.fetchFoods();
    notifyListeners();
  }
}
