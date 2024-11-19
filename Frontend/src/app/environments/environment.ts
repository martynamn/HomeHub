// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

import { Environment } from "./ienvironment";

export const environment: Environment = {
  production: false,
  baseHref: "",
  defaultLang: "en",
  supportedLang: ["en", "pl"],
  authDebug: true,
  brand: {
    name: "frontend",
    logoImage: "logo-main.svg",
  },

  apiUrl: "/api/",
  keyCloakConstructParams: {
    url: "http://localhost:8080/" /* Authorization server URL */,
    realm: "Test",
    clientId: "frontend-test",
    "ssl-required": "external",
    "public-client": true,
    "auth-server-url": "http://localhost:8080/" /* Authorization server URL */,
    "confidential-port": 0,
    resource: "frontend-test",
    logoutUrl: "http://localhost:4200" /* Redirection URI after logout() */,
    redirect_uri:
      "http://localhost:4200" /* Redirection URI after failed KC operation */,
  },
  keyCloakInitParams: {
    onLoad: "login-required",
    checkLoginIframe: false,
    promiseType: "native",
  },
  authConfig: {
    authRequired: true,
    authHttp: true,
    tokenValidUntilTime: 60,
    tokenAutoRefresh: true,
  },
};

