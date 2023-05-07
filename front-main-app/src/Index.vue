<script setup lang="ts">
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();
onMounted(() => {});
</script>
<script lang="ts">
(function ($) {
  $(document).ready(function () {
    /* 点击控制侧边栏 */
    var $wrapper = $(".wrapper");

    /*Counter Animation*/
    var counterAnim = $(".counter-anim");
    if (counterAnim.length > 0) {
      counterAnim.counterUp({ delay: 10, time: 1000 });
    }

    /*Tooltip*/
    if ($('[data-toggle="tooltip"]').length > 0)
      $('[data-toggle="tooltip"]').tooltip();

    /*Popover*/
    if ($('[data-toggle="popover"]').length > 0)
      $('[data-toggle="popover"]').popover();

    /*Sidebar Collapse Animation*/
    var sidebarNavCollapse = $(".fixed-sidebar-left .side-nav  li .collapse");
    var sidebarNavAnchor = ".fixed-sidebar-left .side-nav  li a";
    $(document).on("click", sidebarNavAnchor, function (e) {
      // @ts-ignore
      if ($(this).attr("aria-expanded") === "false") $(this).blur();
      // @ts-ignore
      $(sidebarNavCollapse).not($(this).parent().parent()).collapse("hide");
    });

    /*Panel Remove*/
    $(document).on("click", ".close-panel", function (e) {
      // @ts-ignore
      var effect = $(this).data("effect");
      // @ts-ignore
      $(this).closest(".panel")[effect]();
      return false;
    });

    /*Accordion js*/
    $(document).on("show.bs.collapse", ".panel-collapse", function (e) {
      // @ts-ignore
      $(this).siblings(".panel-heading").addClass("activestate");
    });

    $(document).on("hide.bs.collapse", ".panel-collapse", function (e) {
      // @ts-ignore
      $(this).siblings(".panel-heading").removeClass("activestate");
    });

    /*Sidebar Navigation*/
    $(document).on(
      "click",
      "#toggle_nav_btn,#open_right_sidebar,#setting_panel_btn",
      function (e) {
        $(".dropdown.open > .dropdown-toggle").dropdown("toggle");
        return false;
      }
    );
    $(document).on("click", "#toggle_nav_btn", function (e) {
      $wrapper
        .removeClass("open-right-sidebar open-setting-panel")
        .toggleClass("slide-nav-toggle");
      return false;
    });

    $(document).on("click", "#open_right_sidebar", function (e) {
      $wrapper
        .toggleClass("open-right-sidebar")
        .removeClass("open-setting-panel");
      return false;
    });

    $(document).on("click", ".product-carousel .owl-nav", function (e) {
      return false;
    });

    $(document).on("click", "body", function (e) {
      if (
        $(e.target).closest(".fixed-sidebar-right,.setting-panel").length > 0
      ) {
        return;
      }
      $("body > .wrapper").removeClass("open-right-sidebar open-setting-panel");
      return;
    });

    $(document).on(
      "show.bs.dropdown",
      ".nav.navbar-right.top-nav .dropdown",
      function (e) {
        $wrapper.removeClass("open-right-sidebar open-setting-panel");
        return;
      }
    );

    $(document).on("click", "#setting_panel_btn", function (e) {
      $wrapper
        .toggleClass("open-setting-panel")
        .removeClass("open-right-sidebar");
      return false;
    });
    $(document).on("click", "#toggle_mobile_nav", function (e) {
      $wrapper.toggleClass("mobile-nav-open").removeClass("open-right-sidebar");
      return;
    });

    $(document).on(
      "mouseenter mouseleave",
      ".wrapper > .fixed-sidebar-left",
      function (e) {
        if (e.type == "mouseenter") {
          $wrapper.addClass("sidebar-hover");
        } else {
          $wrapper.removeClass("sidebar-hover");
        }
        return false;
      }
    );

    $(document).on(
      "mouseenter mouseleave",
      ".wrapper > .setting-panel",
      function (e) {
        if (e.type == "mouseenter") {
          $wrapper.addClass("no-transition");
        } else {
          $wrapper.removeClass("no-transition");
        }
        return false;
      }
    );

    /*Todo*/
    var random = Math.random();
    $(document).on("keypress", "#add_todo", function (e) {
      // @ts-ignore
      if (e.which == 13 && !$(this).val().length == 0) {
        $(
          '<li class="todo-item"><div class="checkbox checkbox-success"><input type="checkbox" id="checkbox' +
            random +
            '"/><label for="checkbox' +
            random +
            '">' +
            $(".new-todo input").val() +
            '</label></div></li><li><hr class="light-grey-hr"/></li>'
        ).insertAfter(".todo-list li:last-child");
        $(".new-todo input").val("");
      } else if (e.which == 13) {
        alert("Please type somthing!");
      }
      return;
    });

    /*Chat*/
    $(document).on("keypress", "#input_msg_send", function (e) {
      // @ts-ignore
      if (e.which == 13 && !$(this).val().length == 0) {
        $(
          '<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' +
            // @ts-ignore
            $(this).val() +
            '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>'
        ).insertAfter(".fixed-sidebar-right .chat-content  ul li:last-child");
        // @ts-ignore
        $(this).val("");
      } else if (e.which == 13) {
        alert("Please type somthing!");
      }
      return;
    });
    $(document).on("keypress", "#input_msg_send_widget", function (e) {
      // @ts-ignore
      if (e.which == 13 && !$(this).val().length == 0) {
        $(
          '<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' +
            // @ts-ignore
            $(this).val() +
            '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>'
        ).insertAfter(".chat-for-widgets .chat-content  ul li:last-child");
        // @ts-ignore
        $(this).val("");
      } else if (e.which == 13) {
        alert("Please type somthing!");
      }
      return;
    });
    $(document).on("keypress", "#input_msg_send_chatapp", function (e) {
      // @ts-ignore
      if (e.which == 13 && !$(this).val().length == 0) {
        $(
          '<li class="self mb-10"><div class="self-msg-wrap"><div class="msg block pull-right">' +
            // @ts-ignore
            $(this).val() +
            '<div class="msg-per-detail mt-5"><span class="msg-time txt-grey">3:30 pm</span></div></div></div><div class="clearfix"></div></li>'
        ).insertAfter(".chat-for-widgets-1 .chat-content  ul li:last-child");
        // @ts-ignore
        $(this).val("");
      } else if (e.which == 13) {
        alert("Please type asomthing!");
      }
      return;
    });

    $(document).on(
      "click",
      ".fixed-sidebar-right .chat-cmplt-wrap .chat-data",
      function (e) {
        $(".fixed-sidebar-right .chat-cmplt-wrap").addClass("chat-box-slide");
        return false;
      }
    );
    $(document).on("click", ".fixed-sidebar-right #goto_back", function (e) {
      $(".fixed-sidebar-right .chat-cmplt-wrap").removeClass("chat-box-slide");
      return false;
    });

    /*Chat for Widgets*/
    $(document).on(
      "click",
      ".chat-for-widgets.chat-cmplt-wrap .chat-data",
      function (e) {
        $(".chat-for-widgets.chat-cmplt-wrap").addClass("chat-box-slide");
        return false;
      }
    );
    $(document).on("click", "#goto_back_widget", function (e) {
      $(".chat-for-widgets.chat-cmplt-wrap").removeClass("chat-box-slide");
      return false;
    });
    /*Horizontal Nav*/
    $(document).on(
      "show.bs.collapse",
      ".top-fixed-nav .fixed-sidebar-left .side-nav > li > ul",
      function (e) {
        e.preventDefault();
      }
    );

    /*Slimscroll*/
    $(".nicescroll-bar").slimscroll({
      height: "100%",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
      size: "4px",
      alwaysVisible: false,
    });
    $(".message-nicescroll-bar").slimscroll({
      height: "229px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".message-box-nicescroll-bar").slimscroll({
      height: "350px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".product-nicescroll-bar").slimscroll({
      height: "346px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".app-nicescroll-bar").slimscroll({
      height: "162px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".todo-box-nicescroll-bar").slimscroll({
      height: "310px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".users-nicescroll-bar").slimscroll({
      height: "370px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".users-chat-nicescroll-bar").slimscroll({
      height: "257px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".chatapp-nicescroll-bar").slimscroll({
      height: "543px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });
    $(".chatapp-chat-nicescroll-bar").slimscroll({
      height: "483px",
      size: "4px",
      color: "#878787",
      disableFadeOut: true,
      borderRadius: 0,
    });

    /*Product carousel*/
    if ($(".product-carousel").length > 0)
      var $owl = $(".product-carousel").owlCarousel({
        loop: true,
        margin: 15,
        nav: true,
        navText: [
          "<i class='zmdi zmdi-chevron-left'></i>",
          "<i class='zmdi zmdi-chevron-right'></i>",
        ],
        dots: false,
        autoplay: true,
        responsive: {
          0: {
            items: 1,
          },
          400: {
            items: 2,
          },
          767: {
            items: 3,
          },
          1399: {
            items: 4,
          },
        },
      });

    /*Refresh Init Js*/
    var refreshMe = ".refresh";
    $(document).on("click", refreshMe, function (e) {
      // @ts-ignore
      var panelToRefresh = $(this).closest(".panel").find(".refresh-container");
      // @ts-ignore
      var dataToRefresh = $(this).closest(".panel").find(".panel-wrapper");
      var loadingAnim = panelToRefresh.find(".la-anim-1");
      panelToRefresh.show();
      setTimeout(function () {
        loadingAnim.addClass("la-animate");
      }, 100);
      function started() {} //function before timeout
      setTimeout(function () {
        function completed() {} //function after timeout
        panelToRefresh.fadeOut(800);
        setTimeout(function () {
          loadingAnim.removeClass("la-animate");
        }, 800);
      }, 1500);
      return false;
    });

    /*Fullscreen Init Js*/
    $(document).on("click", ".full-screen", function (e) {
      // @ts-ignore
      $(this).parents(".panel").toggleClass("fullscreen");
      $(window).trigger("resize");
      return false;
    });

    /*Nav Tab Responsive Js*/
    $(document).on(
      "show.bs.tab",
      '.nav-tabs-responsive [data-toggle="tab"]',
      function (e) {
        var $target = $(e.target);
        var $tabs = $target.closest(".nav-tabs-responsive");
        var $current = $target.closest("li");
        var $parent = $current.closest("li.dropdown");
        $current = $parent.length > 0 ? $parent : $current;
        var $next = $current.next();
        var $prev = $current.prev();
        $tabs.find(">li").removeClass("next prev");
        $prev.addClass("prev");
        $next.addClass("next");
        return;
      }
    );

    /* 点击的动画效果开始！ */
    var dropdownSelectors = $(".dropdown, .dropup");

    // Custom function to read dropdown data
    // =========================
    function dropdownEffectData(target) {
      // @todo - page level global?
      var effectInDefault = null,
        effectOutDefault = null;
      var dropdown = $(target),
        dropdownMenu = $(".dropdown-menu", target);
      var parentUl = dropdown.parents("ul.nav");

      // If parent is ul.nav allow global effect settings
      if (parentUl.size() > 0) {
        effectInDefault = parentUl.data("dropdown-in") || null;
        effectOutDefault = parentUl.data("dropdown-out") || null;
      }

      return {
        target: target,
        dropdown: dropdown,
        dropdownMenu: dropdownMenu,
        effectIn: dropdownMenu.data("dropdown-in") || effectInDefault,
        effectOut: dropdownMenu.data("dropdown-out") || effectOutDefault,
      };
    }

    // Custom function to start effect (in or out)
    // =========================
    function dropdownEffectStart(data, effectToStart) {
      if (effectToStart) {
        data.dropdown.addClass("dropdown-animating");
        data.dropdownMenu.addClass("animated");
        data.dropdownMenu.addClass(effectToStart);
      }
    }

    // Custom function to read when animation is over
    // =========================
    function dropdownEffectEnd(data, callbackFunc) {
      var animationEnd =
        "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";
      data.dropdown.one(animationEnd, function () {
        data.dropdown.removeClass("dropdown-animating");
        data.dropdownMenu.removeClass("animated");
        data.dropdownMenu.removeClass(data.effectIn);
        data.dropdownMenu.removeClass(data.effectOut);

        // Custom callback option, used to remove open class in out effect
        if (typeof callbackFunc == "function") {
          callbackFunc();
        }
      });
    }

    // Bootstrap API hooks
    // =========================
    dropdownSelectors.on({
      "show.bs.dropdown": function () {
        // On show, start in effect
        var dropdown = dropdownEffectData(this);
        dropdownEffectStart(dropdown, dropdown.effectIn);
      },
      "shown.bs.dropdown": function () {
        // On shown, remove in effect once complete
        var dropdown = dropdownEffectData(this);
        if (dropdown.effectIn && dropdown.effectOut) {
          dropdownEffectEnd(dropdown, function () {});
        }
      },
      "hide.bs.dropdown": function (e) {
        // On hide, start out effect
        var dropdown = dropdownEffectData(this);
        if (dropdown.effectOut) {
          e.preventDefault();
          dropdownEffectStart(dropdown, dropdown.effectOut);
          dropdownEffectEnd(dropdown, function () {
            dropdown.dropdown.removeClass("open");
          });
        }
      },
    });
  });
  //@ts-ignore
})(jQuery);
</script>
<template>
  <!-- Preloader -->
  <div class="preloader-it">
    <div class="la-anim-1"></div>
  </div>
  <!-- /Preloader -->
  <div class="wrapper theme-1-active pimary-color-blue">
    <NavBar></NavBar>
    <SideBar></SideBar>
    <!-- Right Sidebar Menu -->
    <div class="fixed-sidebar-right">
      <ul class="right-sidebar">
        <li>
          <div class="tab-struct custom-tab-1">
            <ul role="tablist" class="nav nav-tabs" id="right_sidebar_tab">
              <li class="active" role="presentation">
                <a
                  aria-expanded="true"
                  data-toggle="tab"
                  role="tab"
                  id="chat_tab_btn"
                  href="#chat_tab"
                  >chat</a
                >
              </li>
              <li role="presentation" class="">
                <a
                  data-toggle="tab"
                  id="messages_tab_btn"
                  role="tab"
                  href="#messages_tab"
                  aria-expanded="false"
                  >messages</a
                >
              </li>
              <li role="presentation" class="">
                <a
                  data-toggle="tab"
                  id="todo_tab_btn"
                  role="tab"
                  href="#todo_tab"
                  aria-expanded="false"
                  >todo</a
                >
              </li>
            </ul>
            <div class="tab-content" id="right_sidebar_content">
              <div
                id="chat_tab"
                class="tab-pane fade active in"
                role="tabpanel"
              >
                <div class="chat-cmplt-wrap">
                  <div class="chat-box-wrap">
                    <div class="add-friend">
                      <a
                        href="javascript:void(0)"
                        class="inline-block txt-grey"
                      >
                        <i class="zmdi zmdi-more"></i>
                      </a>
                      <span class="inline-block txt-dark">users</span>
                      <a
                        href="javascript:void(0)"
                        class="inline-block text-right txt-grey"
                        ><i class="zmdi zmdi-plus"></i
                      ></a>
                      <div class="clearfix"></div>
                    </div>
                    <form role="search" class="chat-search pl-15 pr-15 pb-15">
                      <div class="input-group">
                        <input
                          type="text"
                          id="example-input1-group2"
                          name="example-input1-group2"
                          class="form-control"
                          placeholder="Search"
                        />
                        <span class="input-group-btn">
                          <button type="button" class="btn btn-default">
                            <i class="zmdi zmdi-search"></i>
                          </button>
                        </span>
                      </div>
                    </form>
                    <div id="chat_list_scroll">
                      <div class="nicescroll-bar">
                        <ul class="chat-list-wrap">
                          <li class="chat-list">
                            <div class="chat-body">
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Clay Masse</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >No one saves us but ourselves.</span
                                    >
                                  </div>
                                  <div class="status away"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Evie Ono</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Unity is strength</span
                                    >
                                  </div>
                                  <div class="status offline"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Madalyn Rascon</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Respect yourself if you would have others
                                      respect you.</span
                                    >
                                  </div>
                                  <div class="status online"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Mitsuko Heid</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >I’m thankful.</span
                                    >
                                  </div>
                                  <div class="status online"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Ezequiel Merideth</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Patience is bitter.</span
                                    >
                                  </div>
                                  <div class="status offline"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Jonnie Metoyer</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Genius is eternal patience.</span
                                    >
                                  </div>
                                  <div class="status online"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Angelic Lauver</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Every burden is a blessing.</span
                                    >
                                  </div>
                                  <div class="status away"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Priscila Shy</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Wise to resolve, and patient to
                                      perform.</span
                                    >
                                  </div>
                                  <div class="status online"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                              <a href="javascript:void(0)">
                                <div class="chat-data">
                                  <img
                                    class="user-img img-circle"
                                    src="/picture/user1.png"
                                    alt="user"
                                  />
                                  <div class="user-data">
                                    <span class="name block capitalize-font"
                                      >Linda Stack</span
                                    >
                                    <span class="time block truncate txt-grey"
                                      >Our patience will achieve more than our
                                      force.</span
                                    >
                                  </div>
                                  <div class="status away"></div>
                                  <div class="clearfix"></div>
                                </div>
                              </a>
                            </div>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                  <div class="recent-chat-box-wrap">
                    <div class="recent-chat-wrap">
                      <div class="panel-heading ma-0">
                        <div class="goto-back">
                          <a
                            id="goto_back"
                            href="javascript:void(0)"
                            class="inline-block txt-grey"
                          >
                            <i class="zmdi zmdi-chevron-left"></i>
                          </a>
                          <span class="inline-block txt-dark">ryan</span>
                          <a
                            href="javascript:void(0)"
                            class="inline-block text-right txt-grey"
                            ><i class="zmdi zmdi-more"></i
                          ></a>
                          <div class="clearfix"></div>
                        </div>
                      </div>
                      <div class="panel-wrapper collapse in">
                        <div class="panel-body pa-0">
                          <div class="chat-content">
                            <ul class="nicescroll-bar pt-20">
                              <li class="friend">
                                <div class="friend-msg-wrap">
                                  <img
                                    class="user-img img-circle block pull-left"
                                    src="/picture/user.png"
                                    alt="user"
                                  />
                                  <div class="msg pull-left">
                                    <p>
                                      Hello Jason, how are you, it's been a long
                                      time since we last met?
                                    </p>
                                    <div class="msg-per-detail text-right">
                                      <span class="msg-time txt-grey"
                                        >2:30 PM</span
                                      >
                                    </div>
                                  </div>
                                  <div class="clearfix"></div>
                                </div>
                              </li>
                              <li class="self mb-10">
                                <div class="self-msg-wrap">
                                  <div class="msg block pull-right">
                                    Oh, hi Sarah I'm have got a new job now and
                                    is going great.
                                    <div class="msg-per-detail text-right">
                                      <span class="msg-time txt-grey"
                                        >2:31 pm</span
                                      >
                                    </div>
                                  </div>
                                  <div class="clearfix"></div>
                                </div>
                              </li>
                              <li class="self">
                                <div class="self-msg-wrap">
                                  <div class="msg block pull-right">
                                    How about you?
                                    <div class="msg-per-detail text-right">
                                      <span class="msg-time txt-grey"
                                        >2:31 pm</span
                                      >
                                    </div>
                                  </div>
                                  <div class="clearfix"></div>
                                </div>
                              </li>
                              <li class="friend">
                                <div class="friend-msg-wrap">
                                  <img
                                    class="user-img img-circle block pull-left"
                                    src="/picture/user.png"
                                    alt="user"
                                  />
                                  <div class="msg pull-left">
                                    <p>Not too bad.</p>
                                    <div class="msg-per-detail text-right">
                                      <span class="msg-time txt-grey"
                                        >2:35 pm</span
                                      >
                                    </div>
                                  </div>
                                  <div class="clearfix"></div>
                                </div>
                              </li>
                            </ul>
                          </div>
                          <div class="input-group">
                            <input
                              type="text"
                              id="input_msg_send"
                              name="send-msg"
                              class="input-msg-send form-control"
                              placeholder="Type something"
                            />
                            <div class="input-group-btn emojis">
                              <div class="dropup">
                                <button
                                  type="button"
                                  class="btn btn-default dropdown-toggle"
                                  data-toggle="dropdown"
                                >
                                  <i class="zmdi zmdi-mood"></i>
                                </button>
                                <ul class="dropdown-menu dropdown-menu-right">
                                  <li>
                                    <a href="javascript:void(0)">Action</a>
                                  </li>
                                  <li>
                                    <a href="javascript:void(0)"
                                      >Another action</a
                                    >
                                  </li>
                                  <li class="divider"></li>
                                  <li>
                                    <a href="javascript:void(0)"
                                      >Separated link</a
                                    >
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <div class="input-group-btn attachment">
                              <div class="fileupload btn btn-default">
                                <i class="zmdi zmdi-attachment-alt"></i>
                                <input type="file" class="upload" />
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div id="messages_tab" class="tab-pane fade" role="tabpanel">
                <div class="message-box-wrap">
                  <div class="msg-search">
                    <a href="javascript:void(0)" class="inline-block txt-grey">
                      <i class="zmdi zmdi-more"></i>
                    </a>
                    <span class="inline-block txt-dark">messages</span>
                    <a
                      href="javascript:void(0)"
                      class="inline-block text-right txt-grey"
                      ><i class="zmdi zmdi-search"></i
                    ></a>
                    <div class="clearfix"></div>
                  </div>
                  <div class="set-height-wrap">
                    <div class="streamline message-box nicescroll-bar">
                      <a href="javascript:void(0)">
                        <div class="sl-item unread-message">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Clay Masse</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >12:28 AM</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Themeforest message sent via your envato market
                              profile</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsu messm
                              quia dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user1.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Evie Ono</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >1 Feb</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Pogody theme support</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user1.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Madalyn Rascon</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >31 Jan</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Congratulations from design nominees</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item unread-message">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user1.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Ezequiel Merideth</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >29 Jan</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Themeforest item support message</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item unread-message">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user1.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Jonnie Metoyer</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >27 Jan</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Help with beavis contact form</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Priscila Shy</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >19 Jan</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject"
                              >Your uploaded theme is been selected</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                      <a href="javascript:void(0)">
                        <div class="sl-item">
                          <div class="sl-avatar avatar avatar-sm avatar-circle">
                            <img
                              class="img-responsive img-circle"
                              src="/picture/user1.png"
                              alt="avatar"
                            />
                          </div>
                          <div class="sl-content">
                            <span
                              class="inline-block capitalize-font pull-left message-per"
                              >Linda Stack</span
                            >
                            <span
                              class="inline-block font-11 pull-right message-time"
                              >13 Jan</span
                            >
                            <div class="clearfix"></div>
                            <span class="truncate message-subject">
                              A new rating has been received</span
                            >
                            <p class="txt-grey truncate">
                              Neque porro quisquam est qui dolorem ipsum quia
                              dolor sit amet, consectetur, adipisci velit
                            </p>
                          </div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <div id="todo_tab" class="tab-pane fade" role="tabpanel">
                <div class="todo-box-wrap">
                  <div class="add-todo">
                    <a href="javascript:void(0)" class="inline-block txt-grey">
                      <i class="zmdi zmdi-more"></i>
                    </a>
                    <span class="inline-block txt-dark">todo list</span>
                    <a
                      href="javascript:void(0)"
                      class="inline-block text-right txt-grey"
                      ><i class="zmdi zmdi-plus"></i
                    ></a>
                    <div class="clearfix"></div>
                  </div>
                  <div class="set-height-wrap">
                    <!-- Todo-List -->
                    <ul class="todo-list nicescroll-bar">
                      <li class="todo-item">
                        <div class="checkbox checkbox-default">
                          <input type="checkbox" id="checkbox01" />
                          <label for="checkbox01"
                            >Record The First Episode</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                      <li class="todo-item">
                        <div class="checkbox checkbox-pink">
                          <input type="checkbox" id="checkbox02" />
                          <label for="checkbox02"
                            >Prepare The Conference Schedule</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                      <li class="todo-item">
                        <div class="checkbox checkbox-warning">
                          <input
                            type="checkbox"
                            id="checkbox03"
                            checked="true"
                          />
                          <label for="checkbox03"
                            >Decide The Live Discussion Time</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                      <li class="todo-item">
                        <div class="checkbox checkbox-success">
                          <input
                            type="checkbox"
                            id="checkbox04"
                            checked="true"
                          />
                          <label for="checkbox04"
                            >Prepare For The Next Project</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                      <li class="todo-item">
                        <div class="checkbox checkbox-danger">
                          <input
                            type="checkbox"
                            id="checkbox05"
                            checked="true"
                          />
                          <label for="checkbox05"
                            >Finish Up AngularJs Tutorial</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                      <li class="todo-item">
                        <div class="checkbox checkbox-purple">
                          <input
                            type="checkbox"
                            id="checkbox06"
                            checked="true"
                          />
                          <label for="checkbox06"
                            >Finish Infinity Project</label
                          >
                        </div>
                      </li>
                      <li>
                        <hr class="light-grey-hr" />
                      </li>
                    </ul>
                    <!-- /Todo-List -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
    <!-- /Right Sidebar Menu -->

    <!-- Main Content -->
    <div class="page-wrapper">
      <!-- /#wrapper -->
      <router-view v-slot="{ Component }">
        <!-- <keep-alive v-if="$route.meta.keepAlive"> -->
        <!-- 只有在一个容器切换时alive才生效，并且只有include可以生效，meta不行 -->
        <keep-alive :include="['Home']">
          <component :is="Component" />
        </keep-alive>
        <!-- <component :is="Component" v-else /> -->
      </router-view>
      <BaseFooter></BaseFooter>
    </div>
    <!-- /Main Content -->
  </div>
</template>

<style lang="scss" scoped>
.page-wrapper{
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
