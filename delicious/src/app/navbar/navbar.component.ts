import { Component } from '@angular/core';
import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css'
})
export class NavbarComponent {
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
