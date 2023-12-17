import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedIn = false;
  private role: string | null = null;

  constructor() {}

  login(username: string, password: string) {
    // Lógica de autenticação (simulação estática)
    if (username === 'vania' && password === 'vanines05') {
      this.isLoggedIn = true;
      this.role = 'user';
    } else if (username === 'mariana' && password === '1234') {
      this.isLoggedIn = true;
      this.role = 'admin';
    } else {
      this.isLoggedIn = false;
      this.role = null;
    }
  }

  logout() {
    this.isLoggedIn = false;
    this.role = null;
  }

  getIsLoggedIn(): boolean {
    return this.isLoggedIn;
  }

  getRole(): string | null {
    return this.role;
  }
}
