import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { MyApiService } from '../my-api.service';

import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-recipe-details',
  templateUrl: './recipe-details.component.html',
  styleUrl: './recipe-details.component.css'
})
export class RecipeDetailsComponent {
  recipedetails: any;
  category: any;
  ratings: any;
  isLoggedIn: boolean;
  isAdmin: boolean;
  isCreator: boolean | undefined;

  solidStar = solidStar;
  emptyStar = emptyStar;
  constructor(private route: ActivatedRoute, private myApiService: MyApiService, private authService: AuthService, private router: Router ){
    this.isLoggedIn = this.authService.getIsLoggedIn();
    this.isAdmin = this.authService.getRole() === 'admin';
  }
  ngOnInit() {
    this.route.params.subscribe(params => {
      const id = params['id'];
      const currentUser = this.authService.getCurrentUser();

      this.myApiService.getRecipesByIdData(id).subscribe(
        (data: any) => {
          this.recipedetails = data;
          console.log(data);
          if(this.recipedetails.user === currentUser.username){
            this.isCreator = true;
          }

        },
        (error: any) => {
          console.error('Error fetching data:', error);
        }
      );

      this.myApiService.getRatingsData().subscribe(
        (data: any) => {
          // Filtra as avaliações para aquelas que correspondem ao ID da receita
          this.ratings = data.filter((rating: any) => rating.receita == id);
          console.log(this.ratings);
        },
        (error: any) => {
          console.error('Error fetching data:', error);
        }
      );
    });
  }


  onDeleteRecipe(id:number){
    this.myApiService.deleteRecipe(id).subscribe(
      (response) =>{
        this.router.navigate(['/myRecipes'])
      }
    )
  }
}
