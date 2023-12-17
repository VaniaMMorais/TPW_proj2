import { Component } from '@angular/core';
import { AuthService } from '../auth.service'; // Substitua pelo caminho correto
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string;
  password: string;

  constructor(private authService: AuthService, private router: Router) {
    this.username = '';
    this.password = '';
  }

  onLogin() {
    console.log("username:", this.username);
    console.log("password:", this.password);
    this.authService.login(this.username, this.password);
    console.log("FEITO")
    this.router.navigate(['/home']);
  }
}