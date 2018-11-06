<template>
  <div id="cmsLink">
    <!-- hier würde ich gerne einen dynamischen pfad zu dem jeweiligen icon haben.
    Der pfad ist unter data.iconLink zu erreichen-->
    <img id="icon" src="../assets/icons/iconCmsIntro.svg" />

      <h4>
        {{ data.title }}
      </h4>
      <p>
        {{ data.subtext }}
      </p>
  </div>
</template>
<script>
  export default {
    name: 'cmsLink',
    props: {
      data: {
        type: Object,
      },
    },
    data () {
      return{
      }
    },
    components: {
    }
  };
</script>
<style>
  #cmsLink {
    border: 2px solid black;
    border-radius: 5px;
    width: 130px;
    height: 180px;
    text-align: center;
    float: left;
    margin: 10px;
  }
  #icon {
    top: 20px;
    position: relative;
  }
</style>
