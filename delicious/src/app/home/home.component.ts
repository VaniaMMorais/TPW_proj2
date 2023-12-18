import { Component, OnInit } from '@angular/core';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent{
  solidStar = solidStar;
  emptyStar = emptyStar;
  animationState = 'fadeInUp';
  animationDelays = ['100ms', '300ms', '700ms', '1000ms'];
  search= faMagnifyingGlass;
  isLoggedIn: boolean;
  isAdmin: boolean;
  

  constructor(private authService: AuthService) {
    this.isLoggedIn = this.authService.getIsLoggedIn();
    this.isAdmin = this.authService.getRole() === 'admin';
  }

  onLogout() {
    this.authService.logout();
    this.isLoggedIn = false;
    this.isAdmin = false;
  }

  
  
}
