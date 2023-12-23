import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CarrosselComponent } from './carrossel/carrossel.component';

import { HomeComponent } from './home/home.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { LoginComponent } from './login/login.component';
import { RouterModule } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AboutUSComponent } from './about-us/about-us.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AdminComponent } from './admin/admin.component';
import { MyRecipesComponent } from './my-recipes/my-recipes.component';
import { MyFridgeComponent } from './my-fridge/my-fridge.component';
import { MyShopListComponent } from './my-shop-list/my-shop-list.component';
import { FavoritesComponent } from './favorites/favorites.component';
import { SettingsComponent } from './settings/settings.component';
import { RecipeDetailsComponent } from './recipe-details/recipe-details.component';
import { SearchResultsComponent } from './search-results/search-results.component';
import { ProfileComponent } from './profile/profile.component';
import { RecipeCardComponent } from './recipe-card/recipe-card.component';
import { initializeApp } from 'firebase/app';


const firebaseConfig = {
  apiKey: "AIzaSyC_G8JZKlOmwvewLisK8GJ7Ste4nZNQBfk",
  authDomain: "delicious-food-blog.firebaseapp.com",
  projectId: "delicious-food-blog",
  storageBucket: "delicious-food-blog.appspot.com",
  messagingSenderId: "566081736003",
  appId: "1:566081736003:web:678dd8e94d29465956b3f6"
};

const app = initializeApp(firebaseConfig);

@NgModule({
  declarations: [
    AppComponent,
    CarrosselComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    AboutUSComponent,
    NavbarComponent,
    AdminComponent,
    MyRecipesComponent,
    MyFridgeComponent,
    MyShopListComponent,
    FavoritesComponent,
    SettingsComponent,
    RecipeDetailsComponent,
    SearchResultsComponent,
    ProfileComponent,
    RecipeCardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FontAwesomeModule,
    RouterModule.forRoot([]),
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  //   HttpClientXsrfModule.withOptions({
  //     cookieName: 'csrftoken',
  //     headerName: 'X-CSRFToken',
  // }),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule { }
