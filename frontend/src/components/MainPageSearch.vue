<template>
  <div id="main-page-search">
    <input
      class="form-control mr-sm-2"
      type="search"
      v-model="searchTerm"
      placeholder="What are you looking for?"
      aria-label="Search"
    >
    <button class="btn btn-outline-success my-2 my-sm-0" type="submit" @click="search()">Search</button>
  </div>
</template>

<script>
export default {
  name: "main-page-search",
  data() {
    return {
      searchTerm: ""
    };
  },
  methods: {
    search: function(term) {
      console.log(term);
      console.log(this.searchTerm);
    }
  }
};
</script>

<style lang="scss">
#main-page-search {
  border: 1px solid hotpink;
}
</style>
