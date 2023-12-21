import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { importProvidersFrom } from '@angular/core';


platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(HttpClientModule),
    importProvidersFrom(
      HttpClientXsrfModule.withOptions({
        cookieName: 'My-Xsrf-Cookie', // Nome personalizado para o cookie
        headerName: 'My-Xsrf-Header', // Nome personalizado para o cabeçalho
      })
    ),
    // ... outros provedores ...
  ]
});
