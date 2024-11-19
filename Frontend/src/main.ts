import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './app/app.module';
import { environment } from './app/environments/environment';
import { KeycloakService } from './app/shared/auth/keycloak.service';
import { enableProdMode } from '@angular/core';

if (environment.production) {
  enableProdMode();
}

if (environment.authConfig.authRequired) {
  KeycloakService.init()
    .then(() => {
      console.log('Keycloak initialized');
      bootstrapFn();
    })
    .catch(e => {
      console.warn(e);
      console.warn('Keycloak failed to initialize \nRe-attempt in 5 seconds...');
      setTimeout(() => {
        window.location.reload();
      }, 5000);
    });
} else {
  bootstrapFn();
}


function bootstrapFn() {
  platformBrowserDynamic().bootstrapModule(AppModule).catch(err => console.log(err));
}
