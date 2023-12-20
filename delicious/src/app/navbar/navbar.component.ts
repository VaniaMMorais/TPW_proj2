import { Component, ElementRef, HostListener } from '@angular/core';
import { faMagnifyingGlass, faStar as solidStar } from '@fortawesome/free-solid-svg-icons';
import { faStar as emptyStar } from '@fortawesome/free-regular-svg-icons';
import { AuthService } from '../auth.service';
import { MyApiService } from '../my-api.service';
import { Router } from '@angular/router';

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
  isProfileDropdownOpen: boolean = false;

  

  constructor(private authService: AuthService, private el: ElementRef,private router: Router) {
    this.isLoggedIn = this.authService.getIsLoggedIn();
    this.isAdmin = this.authService.getRole() === 'admin';
  }

  onLogout() {
    this.authService.logout();
    this.isLoggedIn = false;
    this.isAdmin = false;
  }

  toggleProfileDropdown() {
    this.isProfileDropdownOpen = !this.isProfileDropdownOpen;
  }

  searchRecipes(searchTerm: string): void {
    // Navegar para a página de resultados de pesquisa com o termo de pesquisa como parâmetro de consulta
    this.router.navigate(['/searchResults'], { queryParams: { query: searchTerm } });
  }

}
