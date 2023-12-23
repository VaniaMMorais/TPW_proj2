import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';

import { faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-recipe-card',
  templateUrl: './recipe-card.component.html',
  styleUrls: ['./recipe-card.component.css']
})
export class RecipeCardComponent {

  @Input() recipe: any;
  @Input() recipeId: number = 0;

  solidStar = solidStar;
  emptyStar = emptyStar;

  constructor(private router: Router) {}

  navigateToRecipeDetails(recipeId: number): void {
    // Navegue para a rota '/recipeDetails' com o ID da receita como parâmetro
    this.router.navigate(['/recipeDetails', recipeId]);
  }
}


