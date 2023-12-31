import { Component, OnInit } from '@angular/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { MyApiService } from '../my-api.service';
import { Router } from '@angular/router';

import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit{
  animationState = 'fadeInUp';
  animationDelays = ['100ms', '300ms', '700ms', '1000ms'];
  search= faMagnifyingGlass;
  isLoggedIn: boolean;
  isAdmin: boolean;

  recipes: any;
  user: any;
  welcomeMessage: string | undefined;
  

  constructor(private authService: AuthService, private myApiService: MyApiService, private router: Router) {
    this.isLoggedIn = this.authService.getIsLoggedIn();
    this.isAdmin = this.authService.getRole() === 'admin';
  }

  ngOnInit(): void {
    
    this.myApiService.getRecipesData().subscribe(
      (data: any) => {
        this.recipes = data;
        console.log(data);
      },
      (error: any) => {
        console.error('Error fetching data:', error);
      }
    );

  }

  onLogout() {
    this.authService.logout();
    this.isLoggedIn = false;
    this.isAdmin = false;
  }

  
  
}
