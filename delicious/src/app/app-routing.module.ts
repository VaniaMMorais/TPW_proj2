import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { AppComponent } from './app.component';
import { RegisterComponent } from './register/register.component';
import { AboutUSComponent } from './about-us/about-us.component';
import { AdminComponent } from './admin/admin.component';
import { MyFridgeComponent } from './my-fridge/my-fridge.component';
import { MyRecipesComponent } from './my-recipes/my-recipes.component';
import { MyShopListComponent } from './my-shop-list/my-shop-list.component';
import { SettingsComponent } from './settings/settings.component';
import { FavoritesComponent } from './favorites/favorites.component';
import { RecipeDetailsComponent } from './recipe-details/recipe-details.component';
import { SearchResultsComponent } from './search-results/search-results.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  {path:'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path:'aboutUs', component: AboutUSComponent},
  {path: 'admin', component: AdminComponent},
  {path: 'myFridge', component: MyFridgeComponent},
  {path: 'myRecipes', component: MyRecipesComponent},
  {path: 'myShopList', component: MyShopListComponent},
  {path: 'settings', component: SettingsComponent},
  {path: 'favorites', component: FavoritesComponent},
  {path: 'recipeDetails/:id', component: RecipeDetailsComponent},
  {path: 'searchResults', component: SearchResultsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
