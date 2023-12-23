import { Injectable } from '@angular/core';
import { MyApiService } from './my-api.service';
import { HttpClient, HttpHeaders, HttpResponse } from '@angular/common/http';
import { Observable, map } from 'rxjs';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  }),
};

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private isLoggedIn = false;
  private role: string | null = null;
  private apiUrl = 'http://127.0.0.1:8000';
  // private apiUrl = 'http://proj2tpw.pythonanywhere.com/api-auth/login/';

  

  constructor(private myApiService: MyApiService, private http: HttpClient) {}

  // 
  login(username: string, password: string) {

    return this.http.post<any>(this.apiUrl + '/api/auth/',
      {username, password}, httpOptions).pipe(
        map(user => {
          // const user = response.body;
          if(user && user.token){
            localStorage.setItem("currentUser", JSON.stringify(user));
            this.isLoggedIn = true;
            if(user.username == "mariana"){
              this.role = 'admin'
            }
            else{
              this.role = 'user'
            }
          }
          return user;
        })
      );
  }

  logout() {
    localStorage.removeItem("currentUser")
    location.reload()
  }

  getIsLoggedIn(): boolean {
    return this.isLoggedIn;
  }

  getRole(): string | null {
    return this.role;
  }

  getCurrentUser(): any {
    const currentUserString = localStorage.getItem('currentUser');
    return currentUserString ? JSON.parse(currentUserString) : null;
  }
}


