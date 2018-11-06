<template>
  <div id="home">
    <navbar>

    </navbar>
    <div id="content">
      <div id=title>
        <p>
          Welchen Bereich möchtest du <br />
          heute <b>bearbeiten</b>?
        </p>
      </div>
      <div id="cmsSections">
        <router-link to="/cmsIntro"><a>
          <cmsLink v-bind:data="{
              title: 'Intro',
              subtext: 'Generelle Informationen zu deinem Restaurant',
              iconLink: '../assets/icons/introCmsWe.svg' }">
          </cmsLink>
        </a></router-link>
        <router-link to="/cmsWe"><a>
          <cmsLink v-bind:data="{
              title: 'Wir',
              subtext: 'Informationen über dein Team',
              iconLink: '../assets/icons/iconCmsWe.svg' }">
          </cmsLink>
        </a></router-link>
        <router-link to="/cmsMenu"><a>
          <cmsLink v-bind:data="{
              title: 'Menu',
              subtext: 'Informationen zu deiner Speisekarte',
              iconLink: '../assets/icons/iconCmsMenu.svg' }">
          </cmsLink>
        </a></router-link>
        <router-link to="/cmsWhere"><a>
          <cmsLink v-bind:data="{
              title: 'Wo',
              subtext: 'Der Ort deines Restaurants',
              iconLink: '../assets/icons/iconCmsWhere.svg' }">
          </cmsLink>
        </a></router-link>
        <router-link to="/cmsWhen"><a>
          <cmsLink v-bind:data="{
              title: 'Wann',
              subtext: 'Informationen zu Öffnungszeiten und co.',
              iconLink: '../assets/icons/iconCmsWhen.svg' }">
          </cmsLink>
        </a></router-link>
      </div>
    </div>
    <bottom>

    </bottom>
  </div>
</template>

<script>
import navbar from './navbar'
import cmsLink from './cmsLink'
import bottom from './bottom'

export default {
  name: 'home',
  data() {
    return {
      data: {},
    }
  },
  components: {
    navbar,
    cmsLink,
    bottom,
  },
}
</script>
<style>
  #home a {
    color: inherit;
    text-decoration: none;
  }
  #cmsSections {
    width: 470px;
    margin: auto;
  }

</style>
