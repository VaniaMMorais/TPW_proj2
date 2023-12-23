import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { MyApiService } from '../my-api.service';
import { Router } from '@angular/router';
import { RecipeAddService } from '../recipe-add.service';

@Component({
  selector: 'app-my-recipes',
  templateUrl: './my-recipes.component.html',
  styleUrl: './my-recipes.component.css'
})
export class MyRecipesComponent {
  recipes: any;

  constructor(private authService: AuthService, private myApiService: MyApiService, private router: Router,private recipeAddService: RecipeAddService) {
  }

  ngOnInit(): void {
    const currentUser = this.authService.getCurrentUser();
    this.myApiService.getRecipesData().subscribe(
      (data: any) => {
        this.recipes = data.filter((item: {user :any;}) => item.user === currentUser.username);
        console.log(this.recipes);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );

  }

  openAddRecipeModal(): void {
    this.recipeAddService.openAddRecipeModal();
}
}
