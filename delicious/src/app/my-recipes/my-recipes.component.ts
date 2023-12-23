import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { MyApiService } from '../my-api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-my-recipes',
  templateUrl: './my-recipes.component.html',
  styleUrl: './my-recipes.component.css'
})
export class MyRecipesComponent {
  recipes: any;

  constructor(private authService: AuthService, private myApiService: MyApiService, private router: Router) {
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
}
