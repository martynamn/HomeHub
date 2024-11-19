export interface Environment {
  production: boolean;
  baseHref: string;
  authDebug: boolean;
  defaultLang: string,
  supportedLang: string[],
  brand: {
    name: string;
    logoImage: string;
  };
  apiUrl: string;
  keyCloakConstructParams: {
    url: string /* Authorization server URL */;
    realm: string;
    clientId: string;
    "ssl-required": string;
    "public-client": boolean;
    "auth-server-url": string /* Authorization server URL */;
    "confidential-port": number;
    resource: string;
    logoutUrl: string /* Redirection URI after logout() */;
    redirect_uri: string /* Redirection URI after failed KC operation */;
  };
  keyCloakInitParams: {
    onLoad: string;
    checkLoginIframe: boolean;
    promiseType: string;
  };
  authConfig: {
    authRequired: boolean;
    authHttp: boolean;
    tokenValidUntilTime: number;
    tokenAutoRefresh: boolean;
  };
}
