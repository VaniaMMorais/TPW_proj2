import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MyApiService } from '../my-api.service';

import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-recipe-details',
  templateUrl: './recipe-details.component.html',
  styleUrl: './recipe-details.component.css'
})
export class RecipeDetailsComponent {
  recipedetails: any;
  category: any;
  ratings: any;

  solidStar = solidStar;
  emptyStar = emptyStar;
  constructor(private route: ActivatedRoute, private myApiService: MyApiService ){}
  ngOnInit() {
    this.route.params.subscribe(params => {
      const id = params['id'];

      this.myApiService.getRecipesByIdData(id).subscribe(
        (data: any) => {
          this.recipedetails = data;
          console.log(data);

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


}
