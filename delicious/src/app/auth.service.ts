import { Injectable } from '@angular/core';
import { MyApiService } from './my-api.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedIn = false;
  private role: string | null = null;
  private apiUrl = 'http://127.0.0.1:8000/api-auth/login/';

  constructor(private myApiService: MyApiService, private http: HttpClient) {}

  // 
  login(username: string, password: string) {
    const body = { username, password };
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });
    this.http.post(this.apiUrl, body, { headers, withCredentials: true }).subscribe(
      (response)=>{
        console.log(response)
      }
    );
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
