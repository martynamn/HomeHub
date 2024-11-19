import { Injectable } from '@angular/core';
import {
  HttpEvent, HttpInterceptor, HttpHandler, HttpRequest
} from '@angular/common/http';
import { Observable, from } from 'rxjs';
import { concatMap } from 'rxjs/operators';
import { KeycloakService } from './keycloak.service';
import { KeyCloakTokenResult } from '../types/authTypes';
import { environment } from 'src/app/environments/environment';


/** Pass untouched request through to the next request handler. */
@Injectable()
export class AuthInterceptor implements HttpInterceptor {

  DEBUG_MODE: boolean;

  constructor(private keycloakService: KeycloakService) {
    this.DEBUG_MODE = environment.authDebug;
  }

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (this.DEBUG_MODE) { console.log('Authentication HTTP Interceptor called'); }
    if (environment.authConfig.authRequired === true) {
      const tokenPromise: Promise<KeyCloakTokenResult> = this.keycloakService.getToken();
      const tokenObservable: Observable<KeyCloakTokenResult> = from(tokenPromise);
      return tokenObservable.pipe(
        concatMap(tokenResult => {
          if (tokenResult.success === true) {
            if (this.DEBUG_MODE) {console.log('API with token', tokenResult); }
            if (environment.authConfig.authHttp === true) {
              const clonedReq = req.clone({
                headers: req.headers.append('Authorization', 'Bearer ' + tokenResult.token)
                                    .append('Accept', ['application/json', 'text/plain'])
              });
              return next.handle(clonedReq);
            } else {
              return next.handle(req);
            }
          } else {
            if (this.DEBUG_MODE) { console.warn('Unable to refresh Auth token'); }
            this.keycloakService.clearToken();
            return next.handle(req);
          }
        }));
    } else {
      const clonedReq = req.clone({
        headers: req.headers.append('Accept', ['application/json', 'text/plain'])
      });
      if (environment.authConfig.authHttp === true) {
        return next.handle(clonedReq);
      } else {
        return next.handle(req);
      }
    }
  }
}



