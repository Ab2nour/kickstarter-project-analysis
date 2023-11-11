var_quanti = (
    "day_succ",
    "goal",
    "backers",
    "pledged",
    "duration",
    "updates",
    "comments",
    "rewards",
    "facebook_friends",
    "facebook_shares",
    "creator_projects_created",
    "creator_projects_backed",
    "videos",
    "images",
    "words_description",
    "words_risks_and_challenges",
    "faqs",
    "prj_prom",
    "crt_suc_perc",
    "usr_net_pg_rnk",
    "usr_net_nodes",
    "usr_net_tie",
    "usr_net_bic",
    "1f_plg",
    "1f_bck",
    "1prj_prom",
    "2f_plg",
    "2f_bck",
    "2prj_prom",
    "3f_plg",
    "3f_bck",
    "3prj_prom",
)

var_quali = (
    [f"cat{i}" for i in range(1, 16)]
    + [f"curr{i}" for i in range(1, 7)]
    + ["Status", "facebook_connected", "has_video"]
)
